import numpy as np

def create_smaller_local_data_set(file_path, file_output_path, size=100):
    large_file = np.load(file_path)

    small_file = {}
    for f in large_file.files:
        data = large_file[f]
        small_file[f] = data[:size]

    np.savez(file_output_path, **small_file)
    large_file.close()


def create_smaller_local_data_sets():
    create_smaller_local_data_set('./data/train.npz', './data/train_small.npz')
    create_smaller_local_data_set('./data/dev.npz', './data/dev_small.npz')
    create_smaller_local_data_set('./data/test.npz', './data/test_small.npz')

if __name__ == "__main__":
    print('-'*80)
    print('Creating smaller training file...')
    print('-'*80)
    create_smaller_local_data_sets()
    print('-'*80)
    print('Finished!')
    print('Try running:')
    print("python train.py --name model_name --train_record_file './data/train_small.npz' --batch_size 4 --eval_steps 1500")
    print('-'*80)
