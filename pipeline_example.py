from fanesis import FanesisPipeline

imgs_path = "./data/"
base_path = "./output/"

pipeline = FanesisPipeline()
pipeline(imgs_path, base_path)