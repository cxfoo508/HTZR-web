#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *myfunc(void *args) {
    int rlt = 0
    for(int i=0;i<100;++i){
        rlt+=1;
    }
    return NULL;
}

int main() {
    pthread_t th;
    pthread_create(&th, NULL, myfunc, NULL);
    pthread_join(th, NULL);
    return 0;
}