from utils.Driver import *


def test_airflowlogsvalidation(initiate_driver):

    url=load_config("url")
    launch_browser(str(url))
    mouse_hover('status_Field')
    status=get_attributevalue('status_Field','title')
    print("job status is - ", status)
    assert status == "Success", "Logs validation failed"
    click_btn('View_the_jobs')
    parentwindow=get_current_window()
    switch_to_child_window(parentwindow)
    click_btn('Click_to_view_logs')
    Logstring=get_text('content')
    close_browser()
    write_to_file(Logstring)
    switch_to_window(parentwindow)
    close_all_browser()
    assert "generating secret for digest authentication" in Logstring, "validation failed"
    print("-- validation pass  --")
