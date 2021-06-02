from stonehenge.components.ui import Header, Link


AppHeader = Header(
    left=[
        Link(to="/", label="My Logo"),
    ],
    right=[
        Link(to="/about", label="About"),
        Link(to="/portfolio", label="Portfolio"),
        Link(to="/login", label="Login"),
    ],
    layout="left-right",
)
