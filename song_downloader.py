# Dont wastee your time decoding this
# Tool by GH0STH4CK3R

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzICwgYnM0ICwgdGltZSAsIHJlICxvcw0KZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAgYXMgYlNvdXAgDQppbXBvcnQgeG1sICwgc29ja2V0ICwganNvbiANCmZyb20gdHFkbSBpbXBvcnQgdHFkbQ0KZnJvbSB4bWwgaW1wb3J0IGV0cmVlDQpmcm9tIHhtbC5ldHJlZSBpbXBvcnQgRWxlbWVudFRyZWUNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUgLCBpbml0DQppbml0KCkNCmxnID0gRm9yZS5MSUdIVEdSRUVOX0VYICAgICMgQ29sb3Vycw0KbHkgPSBGb3JlLkxJR0hUWUVMTE9XX0VYDQpsciA9IEZvcmUuTElHSFRSRURfRVgNCg0KZGVmIGNsZWFyKCkgOg0KICAgIGlmIG9zLm5hbWUgPT0gJ250JzoNCiAgICAgICAgb3Muc3lzdGVtKCdjbHMnKQ0KICAgIGVsc2UgOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCg0KYmFubmVyID0gIiIiDQogIOKWiOKWgOKAg+KWiOKWgOKWiOKAg+KWiOKWhCDilojigIPilojiloDiloDigIMg4oCD4paI4paA4paE4oCD4paI4paA4paI4oCD4paIIOKWiCDilojigIPilojiloQg4paI4oCD4paIICDigIPilojiloDilojigIPiloTiloDilojigIPilojiloDiloQNCiAg4paE4paI4oCD4paI4paE4paI4oCD4paIIOKWgOKWiOKAg+KWiOKWhOKWiOKAgyDigIPilojiloTiloDigIPilojiloTilojigIPiloDiloTiloDiloTiloDigIPilogg4paA4paI4oCD4paI4paE4paE4oCD4paI4paE4paI4oCD4paI4paA4paI4oCD4paI4paE4paADQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIiIg0KdGFnID0gIiIiICAgICBbK10gTWFkZSBCeSBHSDBTVEg0Q0szUiAgICAgICBbK10gVmVyc2lvbiAxLjANCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIiIiDQoNCnByaW50KGxnICsgYmFubmVyKQ0KcHJpbnQobHkgKyB0YWcpDQoNCmRlZiByZW1fdGFncyAoc3QpIDoNCg0KICAgIHJldHVybiAnJy5qb2luKHhtbC5ldHJlZS5FbGVtZW50VHJlZS5mcm9tc3RyaW5nKHN0cihzdCkpLml0ZXJ0ZXh0KCkpDQpwcmludCgiXG5UeXBlIFwnSGVscFwnIGZvciBpbnN0cnVjdGlvbnMgIikNCnByaW50KGx5ICsgIiIpDQpzZWFyY2ggPSBpbnB1dCgiXG5TZWFyY2ggU29uZyAgOiAiKQ0KDQppZiBzZWFyY2ggPT0gJ2hlbHAnIG9yIHNlYXJjaCA9PSAnSGVscCcgb3Igc2VhcmNoID09ICdIRUxQJyBvciBzZWFyY2gg'
love = 'CG0tWl1bWlOipvOmMJSlL2ttCG0tWl1VWlN6QDbtVPNtpUWcoaDbVvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFOVMJkjVR1yoaHtYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0wKT4vXD0XVPNtVUOlnJ50XPVtVSA0MKNtJmSqVSAyLKWwnPOuVUAiozptozSgMFVcQDbtVPNtpUWcoaDbVvNtH3EypPOoZy0tIUyjMFO0nTHtL29lpzIwqPOhqJ1vMKVtVvxAPvNtVPOjpzyhqPtvVPOGqTIjVSfmKFOGo25aVUqcoTjtLzHtLKI0o21uqTywLJkfrFOxo3qhoT9uMTIxKT4vXD0XVPNtVUOlnJ50XPVwYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFApovVcQDbtVPNtnJ5jqKDbVvODpzImplNaMJ50MKVaVUEiVTAioaEcoaIyVPRvXD0XVPNtVTAfMJSlXPxAPvNtVPOcoKOipaDtp29hM19xo3qhoT9uMTIlQDcyoUAyVQbAPvNtVPOmMJSlL2ttCFOmMJSlL2thpzIjoTSwMFtaVPpfWl0aXD0XQDc1pzjtCFNvnUE0pUZ6Yl8vX3AyLKWwnPfvYz1jZ3S1LJAeYzAwYlVAPt0XpzImVQ0tpzIkqJImqUZhM2I0XUIloPxtVPNtVPNtVlOGMJSlL2tAPt0XMTS0LFN9VUWypl50MKu0VN0XQDcjLJqyK3AiqKNtCFOvH291pPuxLKEuYPWbqT1fYaOupaAypvVcVPNwVRu0oJjtq2IvVUAwpzSjnJ5aQDbAPzu0oJjtCFOjLJqyK3AiqKNhMzyhMS9uoTjbVzEcqvVfrlWwoTSmplV6Vz1zYJAioaEyoaDvsFxtVPNwVRMcozEcozptL29hqTIhqN0XoTyhn3ZtCKOuM2Isp291pP5znJ5xK2SfoPtvLFVfrlWwoTSmplV6VaIhMUIbLaEhVa0cVPNtVPZtEzyhMTyhMlOfnJ5eQDccVQ0tZN0XQDcjpzyhqPufMlNeVPVvXD0XMz9lVUttnJ4tpzShM2HboTIhXTu0oJjcXFN6QDbtVPNtnQZkVQ0tnUEgoSg4KD0XVPNtVTtmVQ0tnQZkYzMcozEsLJkfXPWbZlVcQDbtVPNtqUE0VQ0tp3ElXTtmJmOqXF5lMKOfLJAyXPp8nQZ+WljaWlxAPvNtVPO0nKEfMFN9VUE0qP5lMKOfLJAyXPp8Y2tmCvpfWlpcQDbtVPNtnJLtWmkuWlOcovO0nKEfMFN6QDbtVPNtVPNtVUAiqKNtCFOvH291pPu0nKEfMFjvnUEgoP5jLKWmMKVvXD0XVPNtVPNtVPO0nKEfMG0bp291pP5uYaA0pzyhMlxAPvNtVPOcMvO0nKEfMG09VvVto3VtqTy0oTH9CFVtVvN6QDbtVPNtVPNtVUEcqTkyVQ0tW1ftGz8tITy0oTHtKFpAPvNtVPOcVPf9VQRAPvNtVPNwDKWupl5bVTM0YvObMJkyozRtGT92MFOGo25ap3jtDaWin2IhVRShM2IfVUjtHUIlMFOZo3MyVUjtG25yVR5cM2u0VTyhVRE1LzScVN0XVPNtVN0X'
god = 'ICAgIHByaW50KCcgWycsaSwnXSAnLHRpdGxlKQ0KICAgIHRpbWUuc2xlZXAoMC4yKSAgICANCg0KdG5vID0gaW50KGlucHV0KCdcblxuRW50ZXIgU29uZyBOdW1iZXIgOiAnKSkNCg0KY19saW5rID0gbGlua3NbdG5vLTFdWydocmVmJ10NCg0KcnVybCA9IHVybCsnY29udmVydC8nDQoNCnl0Y29kZSA9IGNfbGluay5yZXBsYWNlKHJ1cmwsJycpICAgICAgIyBZb3V0dWJlIHZpZGVvIElEDQoNCnl0bGluayA9ICJodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PSIreXRjb2RlICAgI2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9cGFwdXZsVmVaZzgNCg0KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIEhUVFAgUkVRVUVTVCBOTyAxDQoNCnVybDEgPSAiaHR0cHM6Ly95dDFzLmNvbS9hcGkvYWpheFNlYXJjaC9pbmRleCINCg0KZGF0YSA9IHsicSI6IHl0bGluaywidnQiOiAibXAzIn0NCg0KciA9IHJlcXVlc3RzLnBvc3QodXJsMSxkYXRhPWRhdGEpDQoNCnJlc3BvbnNlID0gIGpzb24ubG9hZHMoci50ZXh0KQ0KDQp2aWQgPSByZXNwb25zZVsndmlkJ10gICAgICAgICAgICAgICAgIyBHZXQgdmlkZW8gaWQNCmsgPSByZXNwb25zZVsna2MnXQ0KdGl0bGUgPSByZXNwb25zZVsndGl0bGUnXSAgICAgICAgICAgICMgR2V0IHRpdGxlDQphX3J0aXN0ID0gcmVzcG9uc2VbJ2EnXQ0KcHJpbnQobGcrIlxuVGl0bGUgICAgOiAiLHRpdGxlKQ0KcHJpbnQoIlVwbG9hZGVyIDogIixhX3J0aXN0KQ0KDQojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gSFRUUCBSRVFVRVNUIE5PIDINCg0KdXJsMiA9ICJodHRwczovL3l0MXMuY29tL2FwaS9hamF4Q29udmVydC9jb252ZXJ0Ig0KDQpkYXRhID0geyJ2aWQiOiB2aWQsImsiOiBrfQ0KDQpyMj0gcmVxdWVzdHMucG9zdCh1cmwyLGRhdGE9ZGF0YSkNCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIFNwaW5uZXINCmltcG9ydCBzeXMNCmltcG9ydCB0aW1lDQoNCnByaW50KGx5KyIiKQ0KZGVmIHNwaW5uaW5nX2N1cnNvcigpOg0KDQogICAgY3MgPSBbJ0NvbnZlcnRpbmcgLycsJ0NvbnZlcnRpbmcgLScsJ0NvbnZlcnRpbmcgXFwnLCdDb252ZXJ0aW5nIHwnXQ0KDQogICAgd2hpbGUgVHJ1ZToNCiAg'
destiny = 'VPNtVPNtMz9lVTA1paAipvOcovOwplN6QDbtVPNtVPNtVPNtVPO5nJIfMPOwqKWmo3VAPt0Xp3Ocoz5ypvN9VUAjnJ5hnJ5aK2A1paAipvtcQDczo3VtKlOcovOlLJ5aMFtlZPx6QDbtVPNtp3ymYaA0MT91qP53pzy0MFuhMKu0XUAjnJ5hMKVcXD0XVPNtVUA5pl5mqTEiqKDhMzk1p2tbXD0XVPNtVUEcoJHhp2kyMKNbZP4kXD0XVPNtVUA5pl5mqTEiqKDhq3WcqTHbW1kvKTWpLykvKTWpLykvKTWpLykvKTWpLvpcVPNtVN0XV3A5pl5mqTEiqKDhq3WcqTHbW1kvKTWpLykvKTWpLykvKTWpLykvKTWpLvpcVN0XQDclMKZtCFOdp29hYzkiLJEmXUVlYaEyrUDcQDbAPzEfnJ5eVQ0tpzImJlqxoTyhnlqqVPNtVPNtVPNtVPNtVPNwVRqyqPOxo3qhoT9uMPO1pzjAPvAjpzyhqPulMKZcQDbAPt0XVlNgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVRuHISNtHxIEIHIGIPOBGlNmQDbAPaIloQZtCFOxoTyhnj0XQDcjLKWuoKZtCFO7VzMcoTHvBvOxoTyhn30APt0XpwZtCFOlMKS1MKA0pl5aMKDbqKWfZlkmqUWyLJ09IUW1MFxAPt0XqT5gVQ0tp3ElXUEcqTkyXD0Xp29hM25uoJHtCFO0oz0eVv5gpQZvQDbAPaWwo2EyVQ0tpwZhp3EuqUImK2AiMTHtVPNtVPNtVPNtVPNtVN0XpUWcoaDboTpeVvVcQDccMvOlL29xMFN9CFNlZQNtBt0XVPNtVN0XVPNtVUEiqTSfVQ0tnJ50XUVmYzuyLJEypaZhM2I0XPqwo250MJ50YJkyozq0nPpfVQNcXFNtVPZtHUWiM3Wyp3AvLKVAPvNtVPO3nKEbVT9jMJ4bp29hM25uoJHfVPq3LvpcVTSmVTMcoTHfVUEkMT0bQDbtVPNtVPNtVPNtVPOxMKAwCKAiozqhLJ1yYN0XVPNtVPNtVPNtVPNtqT90LJj9qT90LJjfQDbtVPNtVPNtVPNtVPO1ozy0CFqcDvpfQDbtVPNtVPNtVPNtVPO1ozy0K3AwLJkyCIElqJHfQDbtVPNtVPNtVPNtVPO1ozy0K2Ecqzymo3V9ZGNlAPjAPvNtVPNcVTSmVTWupwbAPvNtVPNtVPNtMz9lVTEuqTRtnJ4tpwZhnKEypy9wo250MJ50XTAbqJ5eK3AcrzH9ZGNlAPx6QDbtVPNtVPNtVPNtVPOmnKcyVQ0tMzyfMF53pzy0MFuxLKEuXFNtVPNtVPNtVPNtVPNtVPNtVPNtVPZtET93ozkiLJEcozpAPvNtVPNtVPNtVPNtVTWupv51pTEuqTHbp2y6MFxAPvNtVPOjpzyhqPtvKT5Ro3qhoT9uMTIxVQ4tVvkmo25aozSgMFxtVPNtVPNtVN0XVPNtVTyhpUI0XPVvXD0XMJkmMFN6QDbtVPNtpUWcoaDbVxEiq25fo2SxVTMunJkyMPNuVPVfpzAiMTHcVPNtVN0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
