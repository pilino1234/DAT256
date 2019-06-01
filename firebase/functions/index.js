const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp();

exports.updateMinifiedUsers = functions.firestore
    .document('users/{userId}')
    .onUpdate(change => {
        const newValue = change.after.data();

        const uid = change.after.id;

        const name = newValue.name;
        const mail = newValue.mail;
        const phonenumber = newValue.phonenumber;

        const newMinifiedUser = {
            name,
            mail,
            phonenumber,
            uid
        };

        updateMinifiedUsersPackages(
            change.after.ref,
            newMinifiedUser
        );

        updateMinifiedUsersDeliveries(
            change.after.ref,
            newMinifiedUser
        );

        return 0;
    });

exports.createMinifiedUsers = functions.firestore
    .document('users/{userId}')
    .onCreate(snap => {
        const newValue = snap.data();

        const uid = snap.id;
        const name = newValue.name;
        const mail = newValue.mail;
        const phonenumber = newValue.phonenumber;

        const newMinifiedUser = {
            name,
            mail,
            phonenumber,
            uid
        };

        updateMinifiedUsers(newMinifiedUser);

        return 0;

    });

exports.createPackages = functions.firestore
    .document('packages/{packageId}')
    .onCreate(snap => {
        updateUsersPackages(snap.data(), snap.id);
        return 0;
    });

exports.updatePackages = functions.firestore
    .document('packages/{packageId}')
    .onUpdate(change => {
        updateUsersPackages(change.after.data(), change.after.id);
        return 0;
    });

function updateUsersPackages(data, packageId){
    const ownerMinifiedUser = data.owner;
    const assistantMinifiedUser = data.assistant;

    updateUserPackage(ownerMinifiedUser.uid, packageId, data);
    try{
        updateUserDelivery(assistantMinifiedUser.uid, packageId, data);
    }catch(e){
        console.log("heeej");
    }
}

function updateUserPackage(userId, packageId, packageData){
    admin.firestore().collection('users').doc(userId).collection('packages').doc(packageId).set(packageData);
}

function updateUserDelivery(userId, packageId, packageData){
    admin.firestore().collection('users').doc(userId).collection('deliveries').doc(packageId).set(packageData);
}

function updateMinifiedUsersPackages(ref, data) {
    ref.collection('packages').get().then(querySnapshot => {
        querySnapshot.forEach(documentSnapshot => {
            documentSnapshot.ref.update({owner: data});
        });
        return 0;
    }).catch(error => {
        console.log(error);
    });
}

function updateMinifiedUsersDeliveries(ref, data) {
    ref.collection('deliveries').get().then(querySnapshot => {
        querySnapshot.forEach(documentSnapshot => {
            documentSnapshot.ref.update({assistant: data});
        });
        return 0;
    }).catch(error => {
        console.log(error);
    });
}