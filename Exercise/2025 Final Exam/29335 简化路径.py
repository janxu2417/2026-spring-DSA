def main():
    path = input().strip().split('/')
    st = []
    for token in path:
        if token == '' or token == '.':
            continue
        if token == '..':
            if st: st.pop()
        else:
            st.append(token)
    print('/' + '/'.join(st))

    return
if __name__ == '__main__':
    main()