import argparse
from pathlib import Path
from DataLoader import Dataloader
from Filters import Filters
from Plotter import Plotter


def main(args):
    # Step 1: Loading image
    loader = Dataloader(args.input_folder)
    images = loader.load_image()

    if not images:
        print(f"No images found in {args.input_folder}")
        return
    
    # Step 2: Plot iamges

    plotter = Plotter(save_dir=Path(args.output_folder))

    for idx, img in enumerate(images):
        inverted = Filters.invert(img)
        thresh = Filters.threshold(img, 100)
        flipped_x = Filters.flip_horizontal(img) 
        flipped_y = Filters.flip_vertical(img)
        sharpen = Filters.sharpen(img)
        
        xx, yy, gaussian_2D = Filters.gaussian_kernel_2D(5, 1.0)
        xx, yy, gaussian_3D = Filters.gaussian_kernel_3D(5, 1.0)

        # Step 3: Plot and save results for each image
        plotter.plot_and_save(img, inverted, "Inverted", f"inverted_{idx}.png")
        plotter.plot_and_save(img, thresh, "Thresholded", f"threshold_{idx}.png")
        plotter.plot_and_save(img, flipped_x, "Flipped_horizontal", f"h_flipped_{idx}.png")
        plotter.plot_and_save(img, flipped_y, "Flipped_vertical", f"v_flipped_{idx}.png")
        plotter.plot_and_save(img, sharpen, "Sharpen", f"sharpen_{idx}.png")
        plotter.plot_filter_and_save(gaussian_2D, "Gaussian_filter_2D(11x11)", f"gaussian_filter_2D(5x5)_{idx}.png")
        plotter.plot_3D(xx, yy, gaussian_3D, "Gaussian_filter_3D(11x11)", f"gaussian_filter_3D(5x5)_{idx}.png")

        print(f"Processed {len(images)} images from {args.input_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="[ComputerVision-2025] Tutorial-1")
    parser.add_argument('--input_folder', default="./images", type=str,
                        help='Path to input folder containing images')
    parser.add_argument('--output_folder', type=str, default="./results",
                        help='Folder to save output results')
    
    args = parser.parse_args()
    main(args)  