"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateFakeJwt = exports.isPasswordMatch = exports.encryptPassword = void 0;
const bcryptjs_1 = __importDefault(require("bcryptjs"));
const config_1 = __importDefault(require("../config/config"));
const jwt = __importStar(require("jsonwebtoken"));
const encryptPassword = async (password) => {
    const encryptedPassword = await bcryptjs_1.default.hash(password, 8);
    return encryptedPassword;
};
exports.encryptPassword = encryptPassword;
const isPasswordMatch = async (password, userPassword) => {
    return bcryptjs_1.default.compare(password, userPassword);
};
exports.isPasswordMatch = isPasswordMatch;
const generateFakeJwt = async () => {
    const fakeUser = {
        userId: 'testUser',
        scopes: ['read', 'write']
    };
    return jwt.sign(fakeUser, config_1.default.jwt.secret, { expiresIn: '1h' });
};
exports.generateFakeJwt = generateFakeJwt;
//# sourceMappingURL=encryption.js.map