import nibabel as nib
import numpy as np
import sys


def mean_std_from_timeseries(in_file: str, out_mean_file: str, out_std_file: str):
    # loading data
    img = nib.load(in_file)
    data = img.get_data()

    newdata1 = data.mean(axis=3)
    newdata2 = data.std(axis=3)

    newimg1 = nib.nifti1.Nifti1Image(newdata1, img.affine, img.header)
    newimg2 = nib.nifti1.Nifti1Image(newdata2, img.affine, img.header)

    nib.save(newimg1, out_mean_file)
    nib.save(newimg2, out_std_file)

    return out_mean_file, out_std_file


if __name__ == "__main__":
    print('\nparam order::\ninput_vol.nii(.gz) output_vol_mean.nii(.gz) output_vol_std.nii(.gz)\n')

    mean_std_from_timeseries(*sys.argv)
