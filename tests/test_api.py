def test_get_all_depts(client):
    '''get all departments'''
    response = client.get('/depts/all')
    assert response != None
    
    