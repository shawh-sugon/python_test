# import Imath
# import OpenEXR
# import numpy as np
#
# exrFile = OpenEXR.InputFile('matilda2.exr')
# header = exrFile.header()
# dw = header['dataWindow']
#
# pt = Imath.PixelType(Imath.PixelType.FLOAT)
# size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
# cc_r = np.fromstring(exrFile.channel('RenderLayer.Combined.R', pt), dtype=np.float32)
# cc_g = np.fromstring(exrFile.channel('RenderLayer.Combined.G', pt), dtype=np.float32)
# cc_b = np.fromstring(exrFile.channel('RenderLayer.Combined.B', pt), dtype=np.float32)
# cc_r.shape = cc_g.shape = cc_b.shape = (size[1], size[0])
# cc = np.dstack((cc_r, cc_g, cc_b))

import numpy
import OpenEXR
import Imath
import imageio
import glob
import os


def ext2tif(exrpath):
    File = OpenEXR.InputFile(exrpath)
    PixType = Imath.PixelType(Imath.PixelType.FLOAT)
    DW = File.header()['dataWindow']
    Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1)
    rgb = [numpy.frombuffer(File.channel(c, PixType), dtype=numpy.float32) for c in 'RGB']
    alpha = [numpy.frombuffer(File.channel(c, PixType), dtype=numpy.float32) for c in 'Alpha']
    print(rgb)
    """
    [
        array([1.        , 1.        , 1.        , ..., 0.42400256, 0.39737388,0.41337353], dtype=float32), 
        array([1.        , 1.        , 1.        , ..., 0.44372487, 0.410274  ,0.45159757], dtype=float32), 
        array([1.        , 1.        , 1.        , ..., 0.39723316, 0.45776173,0.4323282 ], dtype=float32)
    ]
    """
    print(alpha)
    r =numpy.reshape(rgb[0],(Size[1],Size[0]))
    g =numpy.reshape(rgb[1],(Size[1],Size[0]))
    b =numpy.reshape(rgb[2],(Size[1],Size[0]))
    tif = numpy.zeros((Size[1],Size[0],3),dtype=numpy.float32)
    tif[:,:,0] = r
    tif[:,:,1] = g
    tif[:,:,2] = b
    return tif

def writetif(tifpath,tif):
    imageio.imwrite(tifpath,tif,format='tif')



if __name__=="__main__":
    files = glob.glob('./matilda2.exr')
    savepath = './'
    for file in files:
        tif = ext2tif(file)
        filename, file_ext = os.path.splitext(file)
        print(filename,file_ext)
        filename = os.path.basename(filename)
        filename = filename + '.tif'
        curpath = os.path.join(savepath, filename)
        # writetif(curpath,tif)