import pytest
from day09.script import Script

# Given the following distances:
#     London to Dublin = 464
#     London to Belfast = 518
#     Dublin to Belfast = 141
# The possible routes are therefore:
#     Dublin -> London -> Belfast = 982
#     London -> Dublin -> Belfast = 605
#     London -> Belfast -> Dublin = 659
#     Dublin -> Belfast -> London = 659
#     Belfast -> Dublin -> London = 605
#     Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605.

@pytest.mark.parametrize("input,expected", [
    ("London to Dublin = 464",["London","Dublin",464]),
    ("London to Belfast = 518",["London","Belfast",518]),
    ("Dublin to Belfast = 141",["Dublin","Belfast",141])
])
def test_script_get_edge_from_text(input : str, expected : list):
    script = Script()
    edge = script.get_edge_from_text(input)
    assert edge == expected

def test_script_add_edge_to_graph():
    script = Script()
    # 0
    graph = {}
    assert graph == {}
    # 1
    edge = script.get_edge_from_text("London to Dublin = 464")
    script.add_edge_to_graph(graph,edge[0],edge[1],edge[2])
    assert graph == {"London":{"Dublin":464},"Dublin":{"London":464}}
    # 2
    edge = script.get_edge_from_text("London to Belfast = 518")
    script.add_edge_to_graph(graph,edge[0],edge[1],edge[2])
    assert graph == {"London":{"Dublin":464,"Belfast":518},"Dublin":{"London":464},"Belfast":{"London":518}}
    # 3
    edge = script.get_edge_from_text("Dublin to Belfast = 141")
    script.add_edge_to_graph(graph,edge[0],edge[1],edge[2])
    assert graph == {"London":{"Dublin":464,"Belfast":518},"Dublin":{"London":464,"Belfast":141},"Belfast":{"London":518,"Dublin":141}}

@pytest.mark.parametrize("input,expected", [
    ([], {}),
    ([
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141"
    ], {
        "London":{"Dublin":464,"Belfast":518},
        "Dublin":{"London":464,"Belfast":141},
        "Belfast":{"London":518,"Dublin":141}
    })
])
def test_script_get_graph_for_input(input : "list[str]", expected : dict):
    script = Script()
    actual = script.get_graph_for_input(input)
    assert actual == expected