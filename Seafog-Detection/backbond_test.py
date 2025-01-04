#!/usr/bin/env python
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取上上级目录
from detectron2.engine import (
    DefaultTrainer,
    default_argument_parser,
    default_setup,
    launch,
)
from mask2former import (
    add_maskformer2_config,
)
from detectron2.projects.deeplab import add_deeplab_config, build_lr_scheduler
if __name__ == "__main__":
    from mask2former.modeling import D2SwinTransformer
    import torch
    from detectron2.config import get_cfg
    args = default_argument_parser().parse_args()
    cfg = get_cfg()
    add_deeplab_config(cfg)
    add_maskformer2_config(cfg)
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    model = D2SwinTransformer(cfg, input_shape=(3, 224, 224))
    print(model)
    model.train()
    x = torch.randn(2, 3, 224, 224)
    y = model(x)
    for k, v in y.items():
        print(k, v.shape)
    print(model.output_shape())
    print(model.size_divisibility)
    print("Passed")