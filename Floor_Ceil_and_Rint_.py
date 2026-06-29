import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    nums = numpy.array(input().strip().split(' '), float)
    print(numpy.floor(nums))
    print(numpy.ceil(nums))
    print(numpy.rint(nums))
