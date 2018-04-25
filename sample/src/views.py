from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['GET', 'PUT'])
def echo(request, format=None):
    """
    Echo back what the user said
    """
    if request.method == 'GET':
        return Response({'Echo': 'This is the Echo API'})

    elif request.method == 'PUT':
        data=request.data
        if data is None :
            return Response('Nothing supplied to Echo', status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

@api_view(['GET'])
def access(request, format=None):
    """
    Returns whether or not the current user has access to the API 
    """
    if request.method == 'GET':
        API_key = request.META.get('Authorization') # the value is null
        if (API_key) :
           response = check_member_group(API_key)
           return JsonResponse(response)
        else:
            response = check_member_group(API_key)
            #message = 'No Authorization Token supplied' 
            #response = JsonResponse({'status':'false','message':message}, status=404)
            return JsonResponse(response)


@api_view(['GET'])
def token(request, format=None):
    """
    Return the token if it was supplied
    """
    if request.method == 'GET':
        API_key = request.META.get('Authorization') # the value is null
        return Response({'API_key': API_key})


# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See full license at the bottom of this file.
from urllib.parse import quote
import requests
import json
import base64
import logging
import uuid
import datetime
    
# Used for debug logging
logger = logging.getLogger('contacts')

graph_api_endpoint= 'https://graph.microsoft.com/v1.0/'

# Set to False to bypass SSL verification
# Useful for capturing API calls in Fiddler
verifySSL = True
 
# Generic API Sending
def make_api_call(method, url, token, payload = None):
    # Send these headers with all API calls
    headers = { 'User-Agent' : 'pythoncontacts/1.2',
                'Authorization' : 'Bearer {0}'.format(token),
                'Accept' : 'application/json' }
                
    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = { 'client-request-id' : request_id,
                        'return-client-request-id' : 'true' }
                        
    headers.update(instrumentation)
    
    response = None
    
    if (method.upper() == 'GET'):
        logger.debug('{0}: Sending request id: {1}'.format(datetime.datetime.now(), request_id))
        response = requests.get(url, headers = headers, verify = verifySSL)
    elif (method.upper() == 'DELETE'):
        logger.debug('{0}: Sending request id: {1}'.format(datetime.datetime.now(), request_id))
        response = requests.delete(url, headers = headers, verify = verifySSL)
    elif (method.upper() == 'PATCH'):
        headers.update({ 'Content-Type' : 'application/json' })
        logger.debug('{0}: Sending request id: {1}'.format(datetime.datetime.now(), request_id))
        response = requests.patch(url, headers = headers, data = payload, verify = verifySSL)
    elif (method.upper() == 'POST'):
        headers.update({ 'Content-Type' : 'application/json' })
        logger.debug('{0}: Sending request id: {1}'.format(datetime.datetime.now(), request_id))
        response = requests.post(url, headers = headers, data = payload, verify = verifySSL)

    if (not response is None):
        logger.debug('{0}: Request id {1} completed. Server id: {2}, Status: {3}'.format(datetime.datetime.now(), 
                                                                                         request_id,
                                                                                         response.headers.get('request-id'),
                                                                                         response.status_code))
        
    return response
    

# Groups API #
# Gets all the groups the user is a member of
# GET https://graph.microsoft.com/v1.0/me/memberOf
#   parameters:
#     graph_endpoint : string. The URL to the Contacts API endpoint (https://graph.microsoft.com/v1.0/)
#     token: string. The access token  
def check_member_group(token):
    logger.debug('Entering check_member_group.')
    logger.debug('  graph_endpoint: {0}'.format(graph_api_endpoint))
    logger.debug('  token: {0}'.format(token))
                
    check_member_group = '{0}me/memberOf'.format(graph_api_endpoint)
    
    r = make_api_call('GET', check_member_group, token)
    
    logger.debug('Response: {0}'.format(r.json()))
    logger.debug('Leaving check_member_group.')
    
    return r.json()
    
# MIT License: 
 
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# ""Software""), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to 
# the following conditions: 
 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software. 
 
# THE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.