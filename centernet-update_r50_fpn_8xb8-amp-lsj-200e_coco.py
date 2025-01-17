auto_scale_lr = dict(base_batch_size=64)
backend_args = None
batch_augments = [
    dict(size=(
        1024,
        1024,
    ), type='BatchFixedSizePad'),
]
data_root = 'data/coco/'
dataset_type = 'CharacterDataset'
default_hooks = dict(
    checkpoint=dict(interval=1, max_keep_ckpts=2, type='CheckpointHook'),
    logger=dict(interval=50, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(type='DetVisualizationHook'))
default_scope = 'mmdet'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
image_size = (
    1024,
    1024,
)
launcher = 'none'
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=True, type='LogProcessor', window_size=50)

max_epochs = 25
model = dict(
    backbone=dict(
        depth=50,
        frozen_stages=1,
        init_cfg=dict(checkpoint='torchvision://resnet50', type='Pretrained'),
        norm_cfg=dict(requires_grad=True, type='BN'),
        norm_eval=True,
        num_stages=4,
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        style='pytorch',
        type='ResNet'),
    bbox_head=dict(
        feat_channels=256,
        in_channels=256,
        loss_bbox=dict(loss_weight=2.0, type='GIoULoss'),
        loss_cls=dict(
            loss_weight=1.0,
            neg_weight=0.75,
            pos_weight=0.25,
            type='GaussianFocalLoss'),
        num_classes=1,
        stacked_convs=4,
        strides=[
            8,
            16,
            32,
            64,
            128,
        ],
        type='CenterNetUpdateHead'),
    data_preprocessor=dict(
        batch_augments=[
            dict(size=(
                1024,
                1024,
            ), type='BatchFixedSizePad'),
        ],
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_size_divisor=32,
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='DetDataPreprocessor'),
    neck=dict(
        add_extra_convs='on_output',
        in_channels=[
            256,
            512,
            1024,
            2048,
        ],
        init_cfg=dict(layer='Conv2d', type='Caffe2Xavier'),
        num_outs=5,
        out_channels=256,
        relu_before_extra_convs=True,
        start_level=1,
        type='FPN'),
    test_cfg=dict(
        max_per_img=100,
        min_bbox_size=0,
        nms=dict(iou_threshold=0.6, type='nms'),
        nms_pre=1000,
        score_thr=0.05),
    train_cfg=None,
    type='CenterNet')
optim_wrapper = dict(
    optimizer=dict(lr=0.001, momentum=0.9, type='SGD', weight_decay=4e-05),
    paramwise_cfg=dict(norm_decay_mult=0.0),
    type='AmpOptimWrapper')
param_scheduler = [
    dict(
        begin=0,
        by_epoch=False,
        end=4000,
        start_factor=0.00025,
        type='LinearLR'),
    dict(
        begin=0,
        by_epoch=True,
        end=25,
        gamma=0.1,
        milestones=[
            22,
            24,
        ],
        type='MultiStepLR'),
]
resume = False
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='annotations/instances_val2017.json',
        backend_args=None,
        data_prefix=dict(img='val2017/'),
        data_root='data/coco/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file='data/coco/annotations/instances_val2017.json',
    backend_args=None,
    format_only=False,
    metric='bbox',
    type='CocoMetric')
test_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(keep_ratio=True, scale=(
        1333,
        800,
    ), type='Resize'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        meta_keys=(
            'img_id',
            'img_path',
            'ori_shape',
            'img_shape',
            'scale_factor',
        ),
        type='PackDetInputs'),
]
train_cfg = dict(max_epochs=25, type='EpochBasedTrainLoop', val_interval=5)
train_dataloader = dict(
    batch_size=16,
    dataset=dict(
        dataset=dict(
            ann_file='annotations/instances_train2017.json',
            backend_args=None,
            data_prefix=dict(img='train2017/'),
            data_root='data/coco/',
            filter_cfg=dict(filter_empty_gt=True, min_size=32),
            pipeline=[
                dict(backend_args=None, type='LoadImageFromFile'),
                dict(type='LoadAnnotations', with_bbox=True),
                dict(
                    keep_ratio=True,
                    ratio_range=(
                        0.1,
                        2.0,
                    ),
                    scale=(
                        1024,
                        1024,
                    ),
                    type='RandomResize'),
                dict(
                    allow_negative_crop=True,
                    crop_size=(
                        1024,
                        1024,
                    ),
                    crop_type='absolute_range',
                    recompute_bbox=True,
                    type='RandomCrop'),
                dict(min_gt_bbox_wh=(
                    0.01,
                    0.01,
                ), type='FilterAnnotations'),
                dict(prob=0.5, type='RandomFlip'),
                dict(type='PackDetInputs'),
            ],
            type='CocoDataset'),
        times=8,
        type='RepeatDataset'),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        keep_ratio=True,
        ratio_range=(
            0.1,
            2.0,
        ),
        scale=(
            1024,
            1024,
        ),
        type='RandomResize'),
    dict(
        allow_negative_crop=True,
        crop_size=(
            1024,
            1024,
        ),
        crop_type='absolute_range',
        recompute_bbox=True,
        type='RandomCrop'),
    dict(min_gt_bbox_wh=(
        0.01,
        0.01,
    ), type='FilterAnnotations'),
    dict(prob=0.5, type='RandomFlip'),
    dict(type='PackDetInputs'),
]
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='annotations/instances_val2017.json',
        backend_args=None,
        data_prefix=dict(img='val2017/'),
        data_root='data/coco/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file='data/coco/annotations/instances_val2017.json',
    backend_args=None,
    format_only=False,
    metric='bbox',
    type='CocoMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='DetLocalVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work_dirs/centernet-update_r50_fpn_8xb8-amp-lsj-200e_coco'
