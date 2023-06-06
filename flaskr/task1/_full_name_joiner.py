class _FullNameJoiner:

    def __init__(self):
        self.__FULL_NAMES = "full_names"
        self.__sorted_full_names = {
            self.__FULL_NAMES: []
        }
        self.__full_names = {}

    def join_names(self, names):
        self.__join_names_and_sort(names)
        return self.__sorted_full_names

    def __join_names_and_sort(self, names):
        first_names = names.get("first_names", [])
        last_names = names.get("last_names", [])

        self.__join_names(first_names, last_names)
        self.__sorted_full_names[self.__FULL_NAMES] = list(self.__get_full_names_sorted_by_id())

    def __join_names(self, first_names, last_names):
        self.__validate(first_names, last_names)
        if len(first_names) >= len(last_names):
            self.__insert_first_names_into_full_names(first_names)
            self.__update_full_names_with_last_names(last_names)
        else:
            self.__insert_last_names_into_full_names(last_names)
            self.__update_full_names_with_first_names(first_names)

    def __get_full_names_sorted_by_id(self):
        sorted_full_names_per_id = dict(sorted(self.__full_names.items(), key=lambda x: x[0]))
        return sorted_full_names_per_id.values()

    def __insert_first_names_into_full_names(self, first_names):
        self.__insert_names_into_full_names(first_names, 1)

    def __insert_last_names_into_full_names(self, last_names):
        self.__insert_names_into_full_names(last_names, 0)

    def __insert_names_into_full_names(self, names, unpaired_index):
        for name_and_id in names:
            self.__insert_into_full_names(name_and_id, unpaired_index)

    def __insert_into_full_names(self, name_and_id, unpaired_index):
        name_id = name_and_id[1]
        name_and_id.insert(unpaired_index, "unpaired")
        self.__full_names[name_id] = name_and_id

    def __update_full_names_with_first_names(self, first_names):
        self.__update_full_names(first_names, 0, 1)

    def __update_full_names_with_last_names(self, last_names):
        self.__update_full_names(last_names, 1, 0)

    def __update_full_names(self, names, insert_index, unpaired_index):
        for name_and_id in names:
            self.__update_or_insert_into_full_names(name_and_id, insert_index, unpaired_index)

    def __update_or_insert_into_full_names(self, name_and_id, name_index, unpaired_index):
        try:
            full_name = self.__full_names[name_and_id[1]]
            full_name[name_index] = name_and_id[0]
        except KeyError:
            self.__insert_into_full_names(name_and_id, unpaired_index)

    def __validate(self, first_names, last_names):
        self.__validate_names(first_names)
        self.__validate_names(last_names)

    @staticmethod
    def __validate_names(names):
        if names:
            for name_and_id in names:
                if len(name_and_id) != 2:
                    raise ValueError(f"Invalid item: {name_and_id}. Name or ID missing!")
                if not name_and_id[1].isnumeric():
                    raise ValueError(f"Invalid item: {name_and_id}. ID not numeric!")

