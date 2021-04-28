#%% necessary packages
import zlib
import zipfile
#%% function_compress()


def compress(file_names):
    print("File Paths:")
    print(file_names)

    source_dir = r"C:\Users\Jeong\Anaconda3\envs\CAB\CAB-data-science\CAB-data-science\python\module2\ecommerce\com\data\ecom-sales/"
    zipfilename = 'Raws.zip'
    output_path = source_dir + zipfilename

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    zf = zipfile.ZipFile(output_path, mode="w")
    try:
        for file_name in file_names:
            # Add file to the zip file
            # first parameter file to zip, second filename in zip
            zf.write(source_dir + file_name, file_name, compress_type=compression)

    except FileNotFoundError:
        print("An error occurred")
    finally:
        # Don't forget to close the file!
        zf.close()


#%% can compress multiple files 
# e.g. file_names = ['1.txt', '2.txt','3.txt']

file_names = ['sales_summary_asin.csv'] #
compress(file_names)