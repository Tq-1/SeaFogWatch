import collections
import torch

def convert_checkpoint(checkpoint_path, output_path):
    # 加载检查点
    checkpoint = torch.load(checkpoint_path, map_location='cpu')

    # 检查并转换 state_dict_ema
    if 'state_dict_ema' in checkpoint:
        if isinstance(checkpoint['state_dict_ema'], collections.OrderedDict):
            checkpoint['state_dict_ema'] = dict(checkpoint['state_dict_ema'])

    # 保存转换后的检查点
    torch.save(checkpoint, output_path)
    print(f"Checkpoint converted and saved to {output_path}")

if __name__ == "__main__":
    # 请根据你的实际路径修改以下内容
    input_checkpoint_path = 'cswin_large_22k_224.pth'  # 输入检查点路径
    output_checkpoint_path = 'cswin_large_22k_224_converted.pth'  # 输出检查点路径
    convert_checkpoint(input_checkpoint_path, output_checkpoint_path)