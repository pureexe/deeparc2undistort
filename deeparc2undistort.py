import os, shutil, tempfile, subprocess, argparse, time, sys
from timeit import default_timer as timer

def check_require_software():
    softwares = ['colmap','colmap2deeparc']
    for software in softwares:
        if shutil.which(software) is None:
            raise Exception('Install "{}" first!'.format(software))

def call_feature_extrator(image_dir,db_path):
    subprocess.call([
        'colmap', 'feature_extractor',
        '--image_path', image_dir,
        '--database_path', db_path,
        '--ImageReader.single_camera_per_folder', '1',
        '--SiftExtraction.estimate_affine_shape', '1',
        '--SiftExtraction.domain_size_pooling', '1'
    ])

def call_feature_matching(db_path):
    matching_file = os.path.join(
        os.path.dirname(sys.modules['deeparc2undistort'].__file__),
        'window5x5_matching_no_duplicate.txt'
    )
    subprocess.call([
        'colmap', 'matches_importer',
        '--database_path', db_path,
        '--match_list_path', matching_file, 
        '--SiftMatching.guided_matching', '1'
    ])

def call_colmap2deeparc(db_path,reference_model,working_dir):
    deeparc_path = os.path.join(working_dir,'colmap_feature.deeparc')
    subprocess.call([
        'colmap2deeparc', 
        '-i', db_path,
        '-r', reference_model,
        '-o', deeparc_path
    ])
    return deeparc_path


def call_our_sfm(deeparc_path,model_dir):
    subprocess.call([
        'sfm',  #need to change to support package later
        '-input', deeparc_path,
        '-output', model_dir
    ])

def call_image_undistorter(image_dir, model_dir, args):
    # colmap image_undistorter --image_path images/ --input_path teabottle_model --output_path dense/
    if args.batch:
        output_path = os.path.join(args.output,os.path.basename(image_dir))
    else:
        output_path = args.output
    subprocess.call([
        'colmap', 'image_undistorter',
        '--image_path', image_dir,
        '--input_path', model_dir,
        '--output_path', output_path
    ])

def main(args):
    start_time = timer()
    check_require_software() 
    queue = [args.input]
    if args.batch:
        queue = [os.path.join(args.input,d) for d in os.listdir(args.input)]
        queue = list(filter(os.path.isdir,queue))
    if args.batch:
        os.mkdir(args.output)
    for image_dir in queue:
        with tempfile.TemporaryDirectory() as working_dir, tempfile.TemporaryDirectory() as model_dir:
            db_path = os.path.join(working_dir,'colmap_feature.db')
            call_feature_extrator(image_dir,db_path)
            call_feature_matching(db_path)
            deeparc_path = call_colmap2deeparc(db_path, args.reference, working_dir)
            call_our_sfm(deeparc_path, model_dir)
            call_image_undistorter(image_dir, model_dir,args)
    print("Running finished in {} seconds".format(timer() - start_time))
        
def entry_point():
    parser = argparse.ArgumentParser(
        description='deeparc2undistort.py - convert colmap into deeparc format')
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        required=True,
        help='directory of image from deeparc (prefer removed background image)',
    )
    parser.add_argument(
        '-r',
        '--reference',
        type=str,
        required=True,
        help='reference model for camera position') 
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        required=True,
        help='output directory')     
    parser.add_argument(
        '-b',
        '--batch',
        dest='batch',
        action='store_true',
        help='do multiple conversation by put every directory of image into input folder'
    )
    parser.set_defaults(batch=False)
    main(parser.parse_args())

if __name__ == '__main__':
    entry_point()