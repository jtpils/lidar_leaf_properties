# -*- coding: utf-8 -*-
"""
@author: Matheus Boni Vicari (matheus.boni.vicari@gmail.com)

"""
from sklearn.neighbors import NearestNeighbors


def set_nbrs_rad(arr, pts, rad, return_dist=True):

    """
    Function to create a set of nearest neighbors indices and their respective
    distances for a set of points.

    Parameters
    ----------
    arr: array
        N-dimensional array to perform the knn search on.
    pts: array
        N-dimensional array to search for on the knn search.
    knn: int
        Number of nearest neighbors to search for.
    return_dist: boolean
        Option to return or not the distances of each neighbor.

    Returns
    -------
    indices: array
        Set of neighbors indices from 'arr' for each entry in 'pts'.
    distance: array
        Distances from each neighbor to each central point in 'pts'.

    """

    # Initiating the nearest neighbors search and fitting it to the input
    # array.
    nbrs = NearestNeighbors(radius=rad, metric='euclidean',
                            algorithm='kd_tree', leaf_size=15,
                            n_jobs=-1).fit(arr)

    # Checking if the function should return the distance as well or only the
    # neighborhood indices.
    if return_dist is True:
        # Obtaining the neighborhood indices and their respective distances
        # from the center point.
        distance, indices = nbrs.radius_neighbors(pts)
        return distance, indices

    elif return_dist is False:
        # Obtaining the neighborhood indices only.
        indices = nbrs.radius_neighbors(pts, return_distance=False)
        return indices


def set_nbrs_knn(arr, pts, knn, return_dist=True):

    """
    Function to create a set of nearest neighbors indices and their respective
    distances for a set of points.

    Parameters
    ----------
    arr: array
        N-dimensional array to perform the knn search on.
    pts: array
        N-dimensional array to search for on the knn search.
    knn: int
        Number of nearest neighbors to search for.
    return_dist: boolean
        Option to return or not the distances of each neighbor.

    Returns
    -------
    indices: array
        Set of neighbors indices from 'arr' for each entry in 'pts'.
    distance: array
        Distances from each neighbor to each central point in 'pts'.

    """

    # Initiating the nearest neighbors search and fitting it to the input
    # array.
    nbrs = NearestNeighbors(n_neighbors=knn, metric='euclidean',
                            algorithm='kd_tree', leaf_size=15,
                            n_jobs=-1).fit(arr)

    # Checking if the function should return the distance as well or only the
    # neighborhood indices.
    if return_dist is True:
        # Obtaining the neighborhood indices and their respective distances
        # from the center point.
        distance, indices = nbrs.kneighbors(pts)
        return distance, indices

    elif return_dist is False:
        # Obtaining the neighborhood indices only.
        indices = nbrs.kneighbors(pts, return_distance=False)
        return indices