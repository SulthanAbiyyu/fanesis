from fanesis import Individualize, Grouping, Visualize

imgs_path = "./data/"
base_path = "./output/"
output_path = "./output/output/"

i = Individualize(imgs_path, base_path)
i.run()

g = Grouping(output_path)
df = g.run()

v = Visualize(output_path)
v.visualize(df)
