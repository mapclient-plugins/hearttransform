'''
Created on May 21, 2015

@author: hsorby
'''
import pydicom
import os
import numpy as np


def extractImageCorners(directory, filename):
    '''
    Extract the image corners from an image that is assumed to be
    a DICOM image.
    Corners are returned as:
      [bl, br, tl, tr]
    '''
    ds = pydicom.read_file(os.path.join(directory, filename))

    pixel_spacing = ds.PixelSpacing
    delta_i = float(pixel_spacing[0])
    delta_j = float(pixel_spacing[1])
    orient = [float(iop) for iop in ds.ImageOrientationPatient]
    pos = [float(ipp) for ipp in ds.ImagePositionPatient]
    rows = ds.Rows
    columns = ds.Columns
    orient_1 = np.array(orient[:3])
    orient_2 = np.array(orient[3:])
    pos = np.array(pos) - delta_i * (0.5 * orient_1 + 0.5 * orient_2)
    A = np.array([orient[0] * delta_i, orient[3] * delta_j, 0, pos[0],
                  orient[1] * delta_i, orient[4] * delta_j, 0, pos[1],
                  orient[2] * delta_i, orient[5] * delta_j, 0, pos[2],
                  0, 0, 0, 1]).reshape(4, 4)
    b_tl = np.array([0, 0, 0, 1])
    b_tr = np.array([rows, 0, 0, 1])
    b_bl = np.array([0, columns, 0, 1])
    b_br = np.array([rows, columns, 0, 1])
    tl = np.dot(A, b_tl)
    tr = np.dot(A, b_tr)
    bl = np.dot(A, b_bl)
    br = np.dot(A, b_br)

    return [bl[:3].tolist(), br[:3].tolist(), tl[:3].tolist(), tr[:3].tolist()]
