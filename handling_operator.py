import re

class HandlingOperator():
    '''
    Class for handling pricelist of all operators
    Also handling dial number to find the operator providing cheapest
    price for it

    The format should not affect the dialed number, they should be the same: 
    (123)456-7890
    123-456-7890
    1234567890 (difficult to read or remember, though...)

    So whatever the format is, just convert them to pure numbers!

    Attributes:
        pricelists (dict): dictionary of operator associated with its own pricelist
        _dial_number (str): string of dialed number provided somewhere
        dial_prefixes (list): list of all prefixes extracted frrom dial number
    '''
    def __init__(self):
        self.pricelists = {}
        self._dial_number = ''
        self.dial_prefixes = []

    def formatter(self, num_str):
        '''
        Return any format of prefixes, dialed number into string containing number only

        Args: 
            num_str (str): string of number / prefix

        Returns:
            string of formatted number
        '''
        return re.sub(r'[^0-9]', '', num_str)

    @property
    def dial_number(self):
        """
        The dial number property
        """
        return self._dial_number
    
    @dial_number.setter
    def dial_number(self, dial_):
        """
        Set dial number when receiving new dial number
        """
        self._dial_number = self.formatter(str(dial_))
        self.dial_prefixes = self.get_all_dial_prefixes()

    def get_all_dial_prefixes(self):
        """
        get list of all prefixes from dialed number
        
        Args:
            None

        Returns:
            list of all prefixes from dial number
        """
        ls = [self._dial_number[:i+1] for i in range(len(self._dial_number)-1)]
        ls.reverse()

        return ls

    def load_pricelist_to_dict(self, pricelist):
        '''
        Load a file containing pricelist into dictionary
        
        Args: 
            pricelist (str): file name
        
        Returns:
            dictionary of key of prefix and value of price
        '''

        d = {}
        with open(pricelist) as f:
            for line in f:
                key, val = line.split()
                key = self.formatter(str(key))
                d[key] = float(val)
        
        return d

    def add_pricelist(self, pricelist):
        '''
        Add pricelist into dictionary of pricelists
        
        Args: 
            pricelist (str): a file of pricelist
        
        Returns:
            None
        '''
        d = self.load_pricelist_to_dict(pricelist)
        if pricelist not in self.pricelists:
            self.pricelists[pricelist] = d

    def add_all_pricelists(self, pricelists):
        '''
        Add all pricelists available into the pricelist dictionary

        Args:
            pricelists (list): a list of pricelist file

        Returns:
            None
        '''
        if isinstance(pricelists, str):
            self.add_pricelist(pricelists)
        elif isinstance(pricelists, list):
            for ls in pricelists:
                self.add_pricelist(ls)

    def find_cheapest_operator(self):
        '''
        Find the operator with the cheapest price for a given dial number

        Args:
            None

        Returns:
            List of names of operator providing the cheapest price for that dial number
        '''
        prices = {}
        for operator, pricelist in self.pricelists.items():
            for prefix in self.dial_prefixes:
                if prefix in pricelist:
                    prices[operator] = pricelist[prefix]
                    break

        if prices:
            min_price = min(prices.values())
            ls_min_prices = [k for k, v in prices.items() if v == min_price]
            return ls_min_prices
        else:
            print('Warning: No operator with minimum price exist with number', self._dial_number)
            return []



