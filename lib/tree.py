class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._dfs_search(self.root, target_id)

    def _dfs_search(self, node, target_id):
        if node is None:
            return None

        if node['id'] == target_id:
            return node

        for child in node['children']:
            result = self._dfs_search(child, target_id)
            if result is not None:
                return result
        
        return None
