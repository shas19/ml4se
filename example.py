def _new_actions(self, node, object):
    """ Returns a list of Actions that will create new objects.
    """
    object = self._data[1]
    items = []
    add = node.get_add(object)
    # return early if there are no items to be added in the tree
    if len(add) == 0:
        return items

    for klass in add:
        prompt = False
        factory = None
        if isinstance(klass, tuple):
            if len(klass) == 2:
                klass, prompt = klass
            elif len(klass) == 3:
                klass, prompt, factory = klass
        add_node = self._node_for_class(klass)
        if add_node is None:
            continue
        class_name = klass.__name__
        name = add_node.get_name(object)
        if name == "":
            name = class_name
        if factory is None:
            factory = klass
        def perform_add(object):
            self._menu_new_node(factory, prompt)
        items.append(Action(name=name, on_perform=perform_add))
    return items