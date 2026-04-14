def extract_node_types(plan_node):
    node_types = [plan_node["Node Type"]]

    for child in plan_node.get("Plans", []):
        node_types.extend(extract_node_types(child))

    return node_types