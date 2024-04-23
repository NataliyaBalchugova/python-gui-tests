from time import sleep

def test_del_group(app):
    app.groups.open_group_editor()
    tree = app.groups.group_editor.window(auto_id="uxAddressTreeView")
    root = tree.tree_root()
    for node in root.children():
        if node.text() == 'New group':
            node.click()
            break
    app.groups.group_editor.window(auto_id="uxDeleteAddressButton").click()
    app.delete_window.window(auto_id="uxDeleteAllRadioButton").click()
    #sleep(0.5)
    app.delete_window.window(auto_id="uxOKAddressButton").click()
    app.groups.group_editor.close()
