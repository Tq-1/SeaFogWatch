#!/bin/bash
#SBATCH -J last_12ep
#SBATCH -p batch
#SBATCH --cpus-per-task=100
#SBATCH --gres=gpu:4
#SBATCH -N 1
#SBATCH -e job-%j.err
#SBATCH -o job-%j.out
sc=1
ns=0.0
mode=points
all_ly=True
no_lb=False
lbns=0.2
out_dir=output/m2f_agentAttention_cswinb_50ep_dn_mask_ns${ns}_sc${sc}_mode_${mode}_aly_${all_ly}_no_lb_${no_lb}_lbns_${lbns}/
mkdir -p $out_dir
echo ${out_dir}/log
export DETECTRON2_DATASETS=datasets && python train_net.py --num-gpus 1 --resume --config-file configs/ade20k/semantic-segmentation/cswin/maskformer2_cswin_base_IN21k_384_bs16_160k_res640.yaml OUTPUT_DIR $out_dir \
	      MODEL.DN.NUM_DN $sc MODEL.DN.NOISE_SCALE $ns MODEL.MASK_FORMER.TRANSFORMER_DECODER_NAME MultiScaleMaskedTransformerDecoderMaskDN  \
	            MODEL.MASK_FORMER.DN_MODE ${mode} MODEL.MASK_FORMER.ALL_LY_DN $all_ly MODEL.MASK_FORMER.DN_NO_LB  ${no_lb}  \
		   MODEL.MASK_FORMER.LB_NOISE_RATIO $lbns  #>> ${out_dir}/log 2>&1



