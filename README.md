# kakao_API
Using KaKao API, send notification message myself.

# Requirments

[Kakao developers](https://developers.kakao.com/) 참고하여 `내 어플리케이션` 만든 후 설정이 필요합니다.

# Usage

(Default) `config_path`: ${home}/.kakao/

### login
``` python
# 최초 시행 시 Refresh_token 발급을 위해 사용합니다.
python login.py
```
> 1. `REST_KEY` 입력  
> 2. 출력되는 URL에 접속 
> 3. 카카오 로그인   
> 4. 이동된 페이지의 URL을 다시 Input으로 입력.  
-> `config_path`에 token 정보를 담은 `config.json` 파일이 생성됩니다.  

<br>

### token_refresh
``` python
# 6시간 마다 만료되는 access_token을 재발급 합니다.
python token_refresh.py
```

### message
``` python
# 자기 자신에게 메세지 보내기
python message.py -m "{메시지}"
```