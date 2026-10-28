import numpy as np


def softmax(x):
    x = np.asarray(x, dtype=float)
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / exp_x.sum(axis=-1, keepdims=True)


def scaled_dot_product_attention(Q, K, V):
    Q, K, V = (np.asarray(x, dtype=float) for x in (Q, K, V))
    if Q.shape[-1] != K.shape[-1] or K.shape[-2] != V.shape[-2]:
        raise ValueError('Q và K phải cùng số chiều; K và V phải cùng số token')
    scores = Q @ np.swapaxes(K, -1, -2) / np.sqrt(K.shape[-1])
    weights = softmax(scores)
    return scores, weights, weights @ V
