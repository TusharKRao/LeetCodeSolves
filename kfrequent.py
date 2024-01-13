import heapq
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    final = []
    def get_max_k_values(input_dict, k):
        return heapq.nlargest(k, input_dict.items(), key=lambda item: item[1])

    def merge_maps(map1, map2):
        merged_map = map1.copy()

        for key, value in map2.items():
            if key in merged_map:
                merged_map[key] += value
            else:
                merged_map[key] = value

        return merged_map


    def tk(nums, map = {}):
        if len(nums) == 1:
            return {nums[0]: 1}
        else:
            l = len(nums)//2
            n1 = nums[:l]
            n2 = nums[l:]
            map = merge_maps(tk(n1, map), tk(n2, map))

        return map

    map = tk(nums)
    map = get_max_k_values(map, k)
    for item in map:
        final.append(item[0])

    return final
