
def find_top_bit(number):
    mask = 0x01
    while mask <= number:
        mask *= 2
    mask /= 2
    return mask

def max_xor(low, high):
    msb_bit = find_top_bit(high)
    mask_bit = msb_bit
    maxval = 0
    while mask_bit > 0:
        lowbit = low & mask_bit
        highbit = high & mask_bit

        # if the bits are different then just move on to the next position
        if lowbit != highbit:
            maxval = maxval | mask_bit
            mask_bit = mask_bit >> 1
            continue

        # if the common bit is a 1
        # remove it from the high byte, unless it's the MSB
        if highbit > 0:
            if high_bit == msb_bit:
                continue
            else:
                maxval = maxval | (~mask_bit)
        # if the common bit is a 0
        # add it to the low byte
        else:
            maxval =

        mask_bit = mask_bit >> 1
    return maxval


low, high = [int(x) for x in raw_input().strip().split()]

print max_xor(low, high)
