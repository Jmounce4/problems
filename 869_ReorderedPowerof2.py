def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        power_set = set()
        for i in range(31):
            power_set.add(''.join(sorted(str(1 << i))))

        if ''.join(sorted(str(n))) in power_set:
            return True
        else:
            return False
