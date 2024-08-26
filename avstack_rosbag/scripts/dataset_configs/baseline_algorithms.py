_base_ = ["baseline_no_algorithms.py"]

rosbag_writer = {
    "bag_name": "baseline",
    "algorithms": {
        "run_perception": True,
        "run_tracking": True,
        "run_fusion": True,
    },
}
