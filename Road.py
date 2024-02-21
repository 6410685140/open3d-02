import open3d as o3d
import numpy as np

path_crop_data = "crop_data.ply"
pcd_crop_data = o3d.io.read_point_cloud(path_crop_data)

o3d.visualization.draw_geometries([pcd_crop_data])

pcd_crop_data.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

colors = np.array(pcd_crop_data.colors)

for i in range(len(colors)):
    if(colors[i][1] > 0.54 and colors[i][2] > 0.59):
        colors[i][0] = 0
        colors[i][1] = 0
        colors[i][2] = 1
    else:
        colors[i][0] = 1
        colors[i][1] = 1
        colors[i][2] = 1

pcd_crop_data.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([pcd_crop_data])
o3d.io.write_point_cloud("crop_data_colors.ply", pcd_crop_data, write_ascii=True)



