import math
import numpy as np
from ursina import *

class Frustum:
    def __init__(self):
        pass

    def normalize_plane(self, plane):
        norm = np.linalg.norm(plane[:3])
        return plane / norm

    def calculate_frustum_planes(self, cam, fov, aspect_ratio, near_distance, far_distance):
        # Tính toán các thông số cần thiết
        half_v_fov = math.radians(fov / 2)
        half_h_fov = math.atan(math.tan(half_v_fov) * aspect_ratio)
        near_height = 2 * math.tan(half_v_fov) * near_distance
        near_width = 2 * math.tan(half_h_fov) * near_distance
        far_height = 2 * math.tan(half_v_fov) * far_distance
        far_width = 2 * math.tan(half_h_fov) * far_distance

        # Tính toán các điểm của frustum
        near_center = cam.world_position + cam.forward * near_distance
        far_center = cam.world_position + cam.forward * far_distance

        up = cam.up * near_height
        right = cam.right * near_width

        # Tính toán 4 điểm của near plane
        ntl = near_center + up - right
        ntr = near_center + up + right
        nbl = near_center - up - right
        nbr = near_center - up + right

        # Tính toán 4 điểm của far plane
        ftl = far_center + cam.up * far_height - cam.right * far_width
        ftr = far_center + cam.up * far_height + cam.right * far_width
        fbl = far_center - cam.up * far_height - cam.right * far_width
        fbr = far_center - cam.up * far_height + cam.right * far_width

        # Tạo các mặt phẳng
        planes = []
        planes.append(Plane(ntr, (ntr - ntl).cross(nbr - ntr)))  # Top plane
        planes.append(Plane(nbl, (nbr - nbl).cross(nbl - ntl)))  # Bottom plane
        planes.append(Plane(ntl, (ntl - nbl).cross(ftl - ntl)))  # Left plane
        planes.append(Plane(nbr, (fbr - nbr).cross(nbr - ntr)))  # Right plane
        planes.append(Plane(ntl, cam.forward))                   # Near plane
        planes.append(Plane(ftr, -cam.forward))                  # Far plane

        return planes

    def is_in_frustum(self, position, projection_matrix, view_matrix):
        for plane in self.calculate_frustum_planes(projection_matrix, view_matrix):
            if not plane.is_in_front(position):
                return False
        return True

class Plane:
    def __init__(self, point, normal):
        self.point = point
        self.normal = normal.normalized()

    def is_in_front(self, position):
        position_vec3 = Vec3(position)
        return (position_vec3 - self.point).dot(self.normal) > 0