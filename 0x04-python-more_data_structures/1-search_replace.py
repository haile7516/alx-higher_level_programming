earch_replace(my_list, search, replace):

        return [replace if value == search else value for value in my_list]
