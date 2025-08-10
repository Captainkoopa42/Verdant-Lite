import sys, os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'verdant-lite')))
from core.MemorySystem import MemorySystem


def test_connect_thoughts_avoids_duplicates_and_updates_weight():
    m = MemorySystem()
    m.add_thought('A', stability=0.5)
    m.add_thought('B', stability=0.5)
    # initial link from add_thought('B')
    m.connect_thoughts('A', 'B', weight=0.9)
    m.connect_thoughts('A', 'B', weight=0.8)
    connections = [c for c in m.memory_store['A']['connections'] if c[0] == 'B']
    assert len(connections) == 1
    assert connections[0][1] == 0.8
