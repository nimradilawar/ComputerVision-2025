import os
import matplotlib.pyplot as plt

class Plotter:

    def __init__(self, save_dir="results"):
        self.save_dir = save_dir
        self.save_dir.mkdir(parents=True, exist_ok=True)
    
    def plot_and_save(self, original, processed, title, filename):
        """Show original and processed image side by side"""
        plt.figure(figsize=(8,4))
        
        plt.subplot(1,2,1)
        plt.imshow(original, cmap="gray")
        plt.title("Original")
        plt.axis("off")
        
        plt.subplot(1,2,2)
        plt.imshow(processed, cmap="gray")
        plt.title(title)
        plt.axis("off")
        
        save_path = os.path.join(self.save_dir, filename)
        plt.savefig(save_path)
        plt.show()

    def plot_filter_and_save(self, filter, title, filename):
        plt.figure(figsize=(5,5))
        plt.imshow(filter, cmap="viridis", interpolation="nearest")
        plt.colorbar(label="Weight")
        plt.title(title)
        # plt.axis("off")

        save_path = os.path.join(self.save_dir, filename)
        plt.savefig(save_path)
        plt.show()


    def plot_3D(self, xx, yy, filter, title, filename):
        
        fig = plt.figure(figsize=(5,5))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(xx, yy, filter, cmap="viridis")
        ax.set_title("Gaussian Kernel (3D surface)")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("Weight")
        plt.title(title)

        save_path = os.path.join(self.save_dir, filename)
        plt.savefig(save_path)
        plt.show()

