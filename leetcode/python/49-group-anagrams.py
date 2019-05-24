class Solution:
    def groupAnagrams(self, strs):
        output = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in output:
                output[key] = [s]
            else:
                output[key].append(s)
        return [output[k] for k in output]