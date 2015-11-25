/****************************************************************************
** Meta object code from reading C++ file 'grimecleaner.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.4.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../GrimeCleanerPro/grimecleaner.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'grimecleaner.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.4.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_grimeCleaner_t {
    QByteArrayData data[8];
    char stringdata[110];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_grimeCleaner_t, stringdata) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_grimeCleaner_t qt_meta_stringdata_grimeCleaner = {
    {
QT_MOC_LITERAL(0, 0, 12), // "grimeCleaner"
QT_MOC_LITERAL(1, 13, 12), // "open_spybots"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 13), // "open_ccleaner"
QT_MOC_LITERAL(4, 41, 17), // "open_malwarebytes"
QT_MOC_LITERAL(5, 59, 14), // "clean_prefetch"
QT_MOC_LITERAL(6, 74, 16), // "install_software"
QT_MOC_LITERAL(7, 91, 18) // "launch_diskcleanup"

    },
    "grimeCleaner\0open_spybots\0\0open_ccleaner\0"
    "open_malwarebytes\0clean_prefetch\0"
    "install_software\0launch_diskcleanup"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_grimeCleaner[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   44,    2, 0x08 /* Private */,
       3,    0,   45,    2, 0x08 /* Private */,
       4,    0,   46,    2, 0x08 /* Private */,
       5,    0,   47,    2, 0x08 /* Private */,
       6,    0,   48,    2, 0x08 /* Private */,
       7,    0,   49,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void grimeCleaner::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        grimeCleaner *_t = static_cast<grimeCleaner *>(_o);
        switch (_id) {
        case 0: _t->open_spybots(); break;
        case 1: _t->open_ccleaner(); break;
        case 2: _t->open_malwarebytes(); break;
        case 3: _t->clean_prefetch(); break;
        case 4: _t->install_software(); break;
        case 5: _t->launch_diskcleanup(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObject grimeCleaner::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_grimeCleaner.data,
      qt_meta_data_grimeCleaner,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *grimeCleaner::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *grimeCleaner::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_grimeCleaner.stringdata))
        return static_cast<void*>(const_cast< grimeCleaner*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int grimeCleaner::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
