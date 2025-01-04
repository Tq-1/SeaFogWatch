import math
import torch
import torch.nn as nn

from .agent_cswin import AgentCSWin
from .d2_base import D2BaseModel

class D2AgCSWinTransformer(D2BaseModel):
    def __init__(
        self,
        img_size=224,
        patch_size=16,
        in_chans=3,
        num_classes=1000,
        embed_dim=96,
        depth=12,
        split_size=[3,5,7],
        num_heads=12,
        mlp_ratio=4.,
        qkv_bias=True,
        qk_scale=None,
        drop_rate=0.,
        attn_drop_rate=0.,
        drop_path_rate=0.,
        norm_layer=nn.LayerNorm,
        use_chk=False,
        **kwargs
    ):
        super().__init__()
        
        self.num_classes = num_classes
        self.num_features = self.embed_dim = embed_dim
        
        self.cswin = AgentCSWin(
            img_size=img_size,
            patch_size=patch_size,
            in_chans=in_chans,
            num_classes=num_classes,
            embed_dim=embed_dim,
            depth=depth,
            split_size=split_size,
            num_heads=num_heads,
            mlp_ratio=mlp_ratio,
            qkv_bias=qkv_bias,
            qk_scale=qk_scale,
            drop_rate=drop_rate,
            attn_drop_rate=attn_drop_rate,
            drop_path_rate=drop_path_rate,
            norm_layer=norm_layer,
            use_chk=use_chk,
            **kwargs
        )

    def forward_features(self, x):
        return self.cswin.forward_features(x)
    
    def forward(self, x):
        x = self.forward_features(x)
        x = self.cswin.head(x)
        return x

    @torch.jit.ignore
    def no_weight_decay(self):
        return {'pos_embed', 'cls_token'} 