def test_equal():
    sq = 'hello world'
    dq = "hello world"
    assert sq == dq

def test_notin():
    names = ["Prince", "Jackson"]
    assert "Prince" in names
    assert "prince" not in names

def test_testTrue():
    nums = [1,2,3]
    assert len(nums) > 0

def test_instance():
    nums = [1,2,3]
    names = ["Prince", "Jackson"]
    assert isinstance(nums, list)
    assert isinstance(names[0], str)
    assert type(nums) == list
    assert type(names[0]) == str

