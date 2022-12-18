import urllib.request
from json import dumps

def foo(world):
	return { 'hello': world }

def test_snapshot_ability(snapshot):
	snapshot.snapshot_dir = 'snapshots'
	snapshot.assert_match(dumps(foo('world')), 'foo_output.txt')

def test_folio_site_against_snapshot(snapshot):
	snapshot.snapshot_dir = 'snapshots'
	with urllib.request.urlopen('https://robynveitch.com/') as response:
		assert response.status == 200
		html = response.read().decode('utf-8')
		snapshot.assert_match(html, 'site_output.txt')
