package binarysearch

// SearchInts searches for a value in a sorted array of ints
func SearchInts(arr []int, value int) int {
	lf, mid, rg := 0, 0, len(arr)-1

	for lf <= rg {
		mid = (rg + lf) / 2

		if arr[mid] < value {
			lf = mid + 1
		} else if arr[mid] > value {
			rg = mid - 1
		} else {
			return mid
		}
	}
	return -1
}
