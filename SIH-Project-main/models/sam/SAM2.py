import numpy as np
from ultralytics import SAM
from skimage import feature

class SAM2:
    def __init__(self, model_name ="sam2_b.pt"):
        self.model = SAM(model_name)

    def process(self, img):
        results = self.model(img)
        MASKS = results[0].masks.data.cpu().numpy().astype(np.uint8) * 255
        edges = []
        for i in range(len(MASKS)):
            exp = MASKS[i]
            bool_arr = exp.astype(bool)
            edge = feature.canny(bool_arr)
            edges.append(edge)

        output_images = []
        red = np.array([0, 0, 255])
        for edge in edges:
            output_image = img.copy()
            m, n = edge.shape
            for i in range(m):
                for j in range(n):
                    if edge[i][j]:
                        output_image[i, j, :] = red
                        if i - 1 >= 0:
                            output_image[i - 1, j, :] = red
                        if j - 1 >= 0:
                            output_image[i, j - 1, :] = red
                        if i + 1 < m:
                            output_image[i + 1, j, :] = red
                        if j + 1 >= n:
                            output_image[i, j + 1, :] = red
            output_images.append(output_image)
        return output_images
