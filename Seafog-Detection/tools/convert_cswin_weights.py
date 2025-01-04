import torch
import argparse
import os

def convert_cswin_weights(src_path, dst_path):
    """Convert CSWin weights to Detectron2 format."""
    checkpoint = torch.load(src_path, map_location="cpu")
    
    if "model" in checkpoint:
        state_dict = checkpoint["model"]
    elif "state_dict" in checkpoint:
        state_dict = checkpoint["state_dict"]
    else:
        state_dict = checkpoint

    # Create new state dict for Detectron2
    new_state_dict = {}
    
    # Convert backbone weights
    for k, v in state_dict.items():
        if k.startswith("backbone."):
            k = k[9:]  # Remove "backbone." prefix
        elif not k.startswith("backbone"):
            continue

        # Handle special cases
        if "relative_position" in k:
            continue  # Skip relative position bias as we don't use it
        
        if "patch_embed" in k:
            k = k.replace("patch_embed", "stage1_conv_embed")
        
        if "blocks" in k:
            stage_idx = int(k.split(".")[0][-1]) - 1
            k = k.replace(f"blocks.{stage_idx}", f"stage{stage_idx+1}")
        
        # Add "backbone." prefix for Detectron2
        new_k = "backbone." + k
        new_state_dict[new_k] = v

    # Create new checkpoint
    new_checkpoint = {
        "model": new_state_dict,
        "__author__": "Cascade",
        "matching_heuristics": True
    }

    # Save converted weights
    torch.save(new_checkpoint, dst_path)
    print(f"Converted weights saved to {dst_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert CSWin weights to Detectron2 format")
    parser.add_argument("--src", required=True, help="Path to source CSWin weights")
    parser.add_argument("--dst", required=True, help="Path to save converted weights")
    args = parser.parse_args()

    convert_cswin_weights(args.src, args.dst)

if __name__ == "__main__":
    main()
