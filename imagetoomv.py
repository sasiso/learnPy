import struct
import PIL


example_file = "C:\\archive\\gitlab\\kinder_app\\src\\hal\\unix\\grayscale2.omv"
output_file = "C:\\archive\\gitlab\\kinder_app\\src\\assay_pipeline\\test\sample_images" \
              "\\20180103_colorimetric_single_color\\raw\\a.omv"

write = True
if not write:

    with open(output_file, 'rb') as f:
        a = f.read(16)
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)
        a = struct.unpack('i', f.read(4))
        print(a)

if write:
    with open("C:\\archive\\gitlab\\kinder_app\\src\\assay_pipeline\\test\sample_images"
              "\\20180103_colorimetric_single_color\\raw\\a.raw", 'rb') as f:
        print(f)

        with open("C:\\archive\\gitlab\\kinder_app\\src\\assay_pipeline\\test\sample_images"
                  "\\20180103_colorimetric_single_color\\raw\\a.omv", 'wb') as f2:
            f2.write(b'OMV IMG STR V1.1')
            f2.write(struct.pack('i', 0))
            f2.write(struct.pack('i', 1280))
            f2.write(struct.pack('i', 960))
            f2.write(struct.pack('i', 2))
            f2.write(struct.pack('i', 6))
            a = f.read()
            while a:
                f2.write(a)
                a = f.read()
