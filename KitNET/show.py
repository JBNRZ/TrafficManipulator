import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
import argparse


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-rf', '--RMSE_file_path', type=str,
                       help="resulting rmse file (.pkl) path, only for execute mode!")
    parse.add_argument('-mf', '--model_file_path', type=str, default='./example/model.pkl',
                       help="for train mode, model is saved into 'mf'; for execute mode, model is loaded from 'mf'")

    arg = parse.parse_args()
    with open(arg.RMSE_file_path, 'rb') as f:
        rmse = pkl.load(f)

    with open(arg.RMSE_file_path, 'wb') as f:
        pkl.dump(rmse, f)

    with open(arg.model_file_path, "rb") as f:
        _ = pkl.load(f)
        _ = pkl.load(f)
        _ = pkl.load(f)
        AD_threshold = pkl.load(f)

    print('AD_threshold:', AD_threshold)
    print('# rmse over AD_t:', rmse[rmse > AD_threshold].shape)
    print('Total number:', len(rmse))
    print("rmse mean:", np.mean(rmse))

    x = np.arange(0, len(rmse), 1)
    plt.figure()
    plt.scatter(x, rmse, s=12, c='r')
    plt.plot(x, [AD_threshold] * len(rmse), c='black', linewidth=2, label="AD_threshold")
    plt.title("RMSE of Test set")
    plt.xlabel('pkt no.')
    plt.ylabel('RMSE in Kitsune')
    plt.legend()
    plt.show()
