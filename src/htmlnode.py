class HTMLNode ():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Code is trying to use the parent class .to_html()")
    
    def props_to_html(self):
        if self.props != None:
            result = ""
            for key, value in self.props.items():
                result += f' {key}="{value}"'
            return result
        return None
    
    def __repr__(self):
        return (f"This HTMLNode object attributes are\ntag:{self.tag}\nvalue:{self.value}\nchildren:{self.children}\nprops:{self.props}")
