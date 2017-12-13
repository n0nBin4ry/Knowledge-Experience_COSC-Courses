// hope you don't mind I changed the theme to a game that's been on my mind a lot. it is still a symmetric linked list just shorter

#include <iostream>
using namespace std;

struct Beast{
    string name; // name of beast
    Beast *forLink; // forward link
    Beast *backLink; // backward link
};

void introPrompt();
bool goingForward();
Beast *createHyruleGuardians();
Beast *createDivineBeast(string name, Beast *forLink, Beast *backLink);
void freeFor(Beast *start);
void freeBack(Beast *start);
void freeBackRecur(Beast *start);
void endPrompt();

int main(){
    introPrompt();
    bool forward(goingForward());
    Beast *res = createHyruleGuardians();
    if (forward) {
        freeFor(res);
    }
    else {
        freeBackRecur(res);
    }
    endPrompt();
    return 0;
}

void introPrompt() {
    bool empty;
    cout << "Welcome to the final for Computer Science 220, I am a program hailing from ancient Hyrule!\n\n"
    "While Link is out trying to manually free the Divine Beasts all he had to do was start me up to do it automatically!\n"
    "That poor fool.. Anyways you can just save him time from doing it yourself.\n\n";
}
// choosing starting Beast (beginning or end of linked list)
bool goingForward() {
    cout << "All you have to do is choose which Divine Beast to start at:\n"
            "[1]: Vah Ruta of The Zora Domain [0]: Vah Rudania of Death Mountain\n";
    while (true) {
        cout << "> ";
        short choice;
        cin >> choice;
        if (choice == 1) {
            cout << "\a";
            return true;
        }
        else if (choice == 0) {
            cout << "\a";
            return false;
        }
        else {
            cout << "That isn't an option, pick again:\n"
                    "[1]: Vah Ruta of The Zora Domain [0]: Vah Rudania of Death Mountain\n";
        }
    }
}
// creating symmetric linked list
Beast *createHyruleGuardians() {
    Beast *bp1 = createDivineBeast("Vah Rudania", NULL, NULL);
    Beast *bp2 = createDivineBeast("Vah Medoh", bp1, NULL);
    bp1->backLink = bp2;
    Beast *bp3 = createDivineBeast("Vah Naboris", bp2, NULL);
    bp2->backLink = bp3;
    Beast *bp4 = createDivineBeast("Vah Ruta", bp3, NULL);
    bp3->backLink = bp4;
    return bp4;
}
//create beast
Beast *createDivineBeast(string name, Beast* forLink, Beast* backLink) {
    Beast *out = new Beast;
    out->name = name;
    out->forLink = forLink;
    out->backLink = backLink;
    return out;
}
// goes through linked list in forward path
void freeFor(Beast *start) {
    for (Beast *bp = start; bp != NULL; bp = bp->forLink) {
        cout << "Freeing " << bp->name << "... ";
        if (bp->backLink == NULL) {
            cout << "It worked! Calamity Ganon has been weakened!\n";
        }
        else if (bp->forLink == NULL) {
            cout << "All of the Divine Beasts have been freed and are now in position. Calamity Ganon is now as weak as he ever will be!\n\n";
        }
        else {
            cout << "Calamity Ganon has been weakened even more!\n";
        }
    }
}
// goes through linked list in backward path
void freeBack(Beast *start) {
    // this extra loop at beginning is needed so that it cycles through and starts at end to move towards beginning
    for (Beast *bp = start; bp != NULL; bp = bp->forLink) {
        start = bp;
    }
    for (Beast *bp = start; bp != NULL; bp = bp->backLink) {
        cout << "Freeing " << bp->name << "... ";
        if (bp->forLink == NULL) {
            cout << "It worked! Calamity Ganon has been weakened!\n";
        }
        else if (bp->backLink == NULL) {
            cout << "All of the Divine Beasts have been freed and are now in position. Calamity Ganon is now as weak as he ever will be!\n\n";
        }
        else {
            cout << "Calamity Ganon has been weakened even more!\n";
        }
    }
}
// according to my classmates you wanted a recursive version of the backwards linked list; the final didn't say so but don't want to risk it
// used in main, replaced freeBack()
void freeBackRecur(Beast *start) {
    if (start->backLink == NULL) {
        for (Beast *bp = start; bp != NULL; bp = bp->forLink) {
            start = bp;
        }
    }
    cout << "Freeing " << start->name << "... ";
    if (start->forLink == NULL) {
        cout << "It worked! Calamity Ganon has been weakened!\n";
    }
    else {
        cout << "Calamity Ganon has been weakened even more!\n";
    }
    if (start->backLink->backLink == NULL) {
        cout << "Freeing " << start->backLink->name << "... "
                "All of the Divine Beasts have been freed and are now in position. Calamity Ganon is now as weak as he ever will be!\n\n";
    }
    else {freeBackRecur(start->backLink);}
}
void endPrompt() {
    cout << "Okay we've done our part. Now that Ganon is in his weakest form our Link should have a chance to destroy him... Goddess help him.\nThank you for helping us save Hyrule!";
}