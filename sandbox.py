import os
import zipfile


class ReleaseKinder(object):
    @staticmethod
    def get_version():
        # todo : Add logic for git describe
        return 'Kinder_1.0'

    def get_package_name(self):
        filename = "Kinder_Embedded_Application_%s.zip" % (self.get_version())
        return filename

    def zip_dir(self, input_dir, output_dir):
        """

        :param input_dir:
        :param output_dir:
        :return:
        """
        assert os.path.exists(input_dir)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        target_file = os.path.join(output_dir, self.get_package_name())
        if os.path.exists(target_file):
            os.unlink(target_file)

        zip_file = zipfile.ZipFile(target_file, 'w', zipfile.ZIP_DEFLATED)

        for root, dirs, files in os.walk(input_dir):
            files = [f for f in files if not f[0] == '.git' and f.endswith('.mpy')]
            dirs[:] = [d for d in dirs if not d[0] == '.git']
            for _file in files:
                absname = os.path.abspath(os.path.join(root, _file))
                arcname = absname[len(input_dir) + 1:]
                zip_file.write(absname, arcname)
                print("zipped %s" % arcname)

        zip_file.close()
        print("done")

        return target_file


    @staticmethod
    def release(input_dir, output_dir):
        """

        :param input_dir: Input directory for build
        :param output_dir: Output directory for build package
        :return:
        """

        print("Input Directory is ", input_dir)
        print("Output Directory is ", output_dir)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        release = ReleaseKinder()
        target_file = release.zip_dir(input_dir=input_dir,
                                      output_dir=output_dir)

        import hashlib

        BLOCKSIZE = 65536
        hasher = hashlib.sha1()
        with open(target_file, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        print(hasher.hexdigest())

        sha_file = target_file + ".sha1"

        with open(sha_file, 'w') as afile:
            afile.write(hasher.hexdigest())
